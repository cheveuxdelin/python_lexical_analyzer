void sort(float a[], int low, int high)
{
    int i;
    int k;
    i = low;
    while (i < high - 1)
    {
        float t;
        k = miniloc(a, i, high);
        t = a[k];
        a[k] = a[i];
        a[i] = t;
        i = i + 1;
    }
    return;
} /* END of sort() */
void readArray(void)
{
    int i;
    s = "Enter a float number: ";
    write(s);
    read(f1);
    while (i < 10)
    {
        s = "Enter an integer number: ";
        write(s);
        read x[i];
        f2[i] = x[i] * f1;
        i = i + 1;
    }
    return;
} /* END of readArray() */
