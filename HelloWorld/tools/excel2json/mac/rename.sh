for f in `find Whole_body_Channel_G -iname "*.png" `; do
    BaseName=`basename $f`
    Dir=`dirname $f`
    mv $f $Dir/"W_"$BaseName
done