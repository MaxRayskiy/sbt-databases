###1. Install and start MongoDB Community Edition on macOS
```
$ brew tap mongodb/brew
$ brew install mongodb-community
$ brew services start mongodb-community
```
###2. Import dataset
```
$ mongoimport --type csv -d FakeNews -c train --headerline --drop train.csv
```
Output:
```
2022-03-09T21:58:15.363+0300    connected to: mongodb://localhost/
2022-03-09T21:58:15.370+0300    dropping: FakeNews.train
2022-03-09T21:58:18.275+0300    20800 document(s) imported successfully. 0 document(s) failed to import.
```
###3. Simple requests
```
$ mongosh
$ use FakeNews
$ db.train.find({label: 1}).limit(5)
$ db.train.find ({id: {$gte : 30}}).limit(5)
$ db.train.find({id: 123})
$ db.train.updateOne({id: 123}, { $set: { title: "Updated title" }})
```
###4. Measure time with and without index
```
$ db.train.explain().find({author: 'Michael Forsythe and Chris Buckley'}).explain("executionStats")
```
executionTimeMillis: 76
```
$ db.train.createIndex({author: 1})
$ db.train.explain().find({author: 'Michael Forsythe and Chris Buckley'}).explain("executionStats")
```
executionTimeMillis: 3