void writeArray(void)
{
    int i;
    i = 0;
    while (i < 10)
    {
        write f2[i];
        i = i + 1;
    }
    return;
} /* END of writeArray() */
void main(void)
{
    s = "Reading Information…..";
    write(s);
    readArray();
    s = "Sorting…..";
    write(s);
    sort(f2, 0, 10);
    s = "Sorted Array:";
    write(s);
    writeArray();
    return;
} /* END of main() */
