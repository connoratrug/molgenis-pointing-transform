def transformTable(sourceDf, tableKey):
    print('--- read data for table ' + tableKey +' ---')

    # Filter column name ends with end with E1_C6 and copy( allow for white space at the end of the col name)
    dfTrans = sourceDf.filter(regex='.*E1_C6$', axis=1).copy()

    # Add 'ID' column to the front of dataframe
    dfTrans.insert(0, 'ID', sourceDf.filter(items=['Study Subject ID']))

    # Add 'E1-C6' suffix to 'ID' cells
    dfTrans['ID'] = dfTrans['ID'].astype(str) + '-E1-C6'
    dfTrans.rename(columns=lambda x: x.replace('_E1_C6', ''), inplace=True)
    
    return dfTrans
