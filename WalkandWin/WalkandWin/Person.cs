﻿namespace WalkandWin
{
    public class Person
    {
        public string Name { get; private set; }
        public int Points { get; private set; }
        public bool IsDone { get; private set; }
        public bool NewUser { get; private set; }
        public DateTime ResetDate { get; private set; }
        public DateTime StartTime { get; private set; }
        public DateTime DueTime { get; private set; }
        public DateTime EndTime { get; private set; }

        public Person(string name, int points, bool isDone, bool newUser)
        {
            Name = name;
            Points = points;
            IsDone = isDone;
            NewUser = newUser;
            ResetDate = DateTime.Today;
            StartTime = DateTime.Today.AddHours(11).AddMinutes(30);
            DueTime = DateTime.Today.AddHours(12).AddMinutes(15);
            EndTime = DateTime.Today.AddHours(12).AddMinutes(15);
        }

        public void NotPressed()
        {
            IsDone = false;
        }

        public void MinusPoints()
        {
            Points -= 10;
        }

        public void PlussPoints()
        {
            Points += 10;
        }

        public void PressedDone()
        {
            IsDone = true;
        }

        public void SetNotNewUser()
        {
            NewUser = false;
        }
        
        public void SetDate(DateTime today)
        {
            ResetDate = today;
        }
        public void UpdateStartTime(string timeString)
        {
            var newStartTime = DateTime.Parse(timeString);
            if (StartTime != newStartTime)
            {
                StartTime = newStartTime;
            }
        }

        public void UpdateDueTime(string timeString)
        {
            var newDueTime = DateTime.Parse(timeString);
            if (DueTime != newDueTime)
            {
                DueTime = newDueTime;
            }
        }

        public void UpdateEndTime(string timeString)
        {
            var newEndTime = DateTime.Parse(timeString);
            if (EndTime != newEndTime)
            {
                EndTime = newEndTime;
            }
        }
        public void ResetDueTime()
        {
            DueTime = DueTime.AddDays(1);
        }
    }
}
