namespace WalkandWin
{
    public class Person
    {
        public string Name { get; private set; }
        public int Points { get; private set; }
        public bool IsDone { get; private set; }
        public bool Finished { get; private set; }

        public Person(string name, int points, bool isDone, bool finished)
        {
            Name = name;
            Points = points;
            IsDone = isDone;
            Finished = finished;
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

        public void Reset()
        {
            Points = 0;
            IsDone = false;
        }

        public void SetNotFinished()
        {
            Finished = false;
        }

        public void SetFinished()
        {
            Finished = true;
        }
    }
}
