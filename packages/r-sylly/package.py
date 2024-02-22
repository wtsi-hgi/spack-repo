# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSylly(RPackage):
	"""Hyphenation and Syllable Counting for Text Analysis

	Provides the hyphenation algorithm used for 'TeX'/'LaTeX' and similar software, as proposed by Liang (1983, <https://tug.org/docs/liang/>). Mainly contains the
                    function hyphen() to be used for hyphenation/syllable counting of text objects. It was originally developed for and part of the 'koRpus' package, but later
                    released as a separate package so it's lighter to have this particular functionality available for other packages. Support for various languages needs be added
                    on-the-fly or by plugin packages (<https://undocumeantit.github.io/repos/>); this package does not include any language specific data. Due to some restrictions
                    on CRAN, the full package sources are only available from the project homepage. To ask for help, report bugs, request features, or discuss the development of
                    the package, please subscribe to the koRpus-dev mailing list (<http://korpusml.reaktanz.de>).
	"""
	
	homepage = "https://reaktanz.de/?c=hacking&s=sylly"
	cran = "sylly" 

	version("0.1-6", md5="be7fea02c7ffe52d24a075cea5ecead2")

	depends_on("r@3:", type=("build", "run"))
