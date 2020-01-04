#!/bin/sh

DST=`dirname "$(readlink -f "$0")"`/..
VERSION=0.1
cd "${DST}"
xgettext \
	--files-from=./i18n/translatable_files.txt \
	--output-dir=./i18n/raw \
	--output=messages.pot \
	--copyright-holder="Rodrigo Severo <rsev@pm.me>, 2020" \
	--package-name="passgen" \
	--package-version="${VERSION}" \
	--msgid-bugs-address="<rsev@pm.me>" \
	--sort-output \
	--indent
cd "${OLDPWD}"
