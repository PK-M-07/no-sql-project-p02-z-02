use('hospitalDB');

db.getCollection('patients').insertMany([
  { 
    'name': 'Marta Zielińska', 
    'age': 29, 
    'height': 168.5, 
    'is_insured': true, 
    'conditions': ['nadciśnienie'], 
    'contact_info': { 'phone': '123456789', 'email': 'marta.z@example.com' },
    'registration_date': new Date('2024-05-01T10:30:00Z'),
    'last_visit': new Date('2024-12-20T15:00:00Z') 
  },
  { 
    'name': 'Jan Kowalski', 
    'age': 45, 
    'height': 175.3, 
    'is_insured': false, 
    'conditions': ['cukrzyca', 'astma'], 
    'contact_info': { 'phone': '987654321', 'email': 'jan.k@example.com' },
    'registration_date': new Date('2024-02-14T09:00:00Z'),
    'last_visit': new Date('2024-11-10T11:00:00Z')
  }
]);

db.getCollection('doctors').insertMany([
  { 
    'name': 'Dr. Adam Kowalski', 
    'experience_years': 15, 
    'salary': 15000.00, 
    'is_available': true, 
    'specializations': ['Kardiologia'], 
    'contact_info': { 'phone': '987654321', 'email': 'adam.k@example.com' },
    'employment_date': new Date('2010-05-01T09:00:00Z'),
    'last_shift': new Date('2024-12-15T08:00:00Z')
  },
  { 
    'name': 'Dr. Anna Nowak', 
    'experience_years': 8, 
    'salary': 12000.00, 
    'is_available': true, 
    'specializations': ['Neurologia'], 
    'contact_info': { 'phone': '321654987', 'email': 'anna.n@example.com' },
    'employment_date': new Date('2016-03-01T10:00:00Z'),
    'last_shift': new Date('2024-12-17T08:30:00Z')
  }
]);

db.getCollection('appointments').insertMany([
  { 
    'patient_id': { $oid: "507f191e810c19729de860ea" },  
    'doctor_id': { $oid: "507f191e810c19729de860eb" },  
    'duration_minutes': 30, 
    'cost': 200.00, 
    'is_completed': false, 
    'symptoms': ['ból w klatce piersiowej', 'duszności'],
    'details': { 'diagnosis': 'Nadciśnienie tętnicze', 'prescription': 'Leki na nadciśnienie' },
    'appointment_date': new Date('2024-12-15T14:30:00Z'),
    'created_at': new Date('2024-12-10T09:00:00Z')
  },
  { 
    'patient_id': { $oid: "507f191e810c19729de860ec" },  
    'doctor_id': { $oid: "507f191e810c19729de860ed" },  
    'duration_minutes': 45, 
    'cost': 250.00, 
    'is_completed': false, 
    'symptoms': ['ból głowy', 'zawroty głowy'],
    'details': { 'diagnosis': 'Migrena', 'prescription': 'Leki przeciwbólowe' },
    'appointment_date': new Date('2024-12-18T11:00:00Z'),
    'created_at': new Date('2024-12-10T10:00:00Z')
  }
]);

const patientsVisitedAfterJanuary1st = db.getCollection('patients').find({
  'last_visit': { $gte: new Date('2024-01-01') }
}).count();

console.log(`${patientsVisitedAfterJanuary1st} patients visited after January 1st, 2024.`);

db.getCollection('appointments').aggregate([
  { 
    $match: { 
      appointment_date: { $gte: new Date('2024-01-01'), $lt: new Date('2025-01-01') } 
    }
  },
  { 
    $group: { 
      _id: '$doctor_id', 
      totalRevenue: { $sum: '$cost' } 
    }
  },
  { 
    $lookup: { 
      from: 'doctors', 
      localField: '_id', 
      foreignField: '_id', 
      as: 'doctorDetails' 
    }
  },
  { 
    $project: { 
      'doctorName': { $arrayElemAt: ['$doctorDetails.name', 0] },
      'totalRevenue': 1 
    }
  }
]);


