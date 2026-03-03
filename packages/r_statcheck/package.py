# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatcheck(RPackage):
	"""Extract Statistics from Articles and Recompute P-Values

	A "spellchecker" for statistics. It checks whether your
    p-values match their accompanying test statistic and degrees of
    freedom. statcheck searches for null-hypothesis significance test
    (NHST) in APA style (e.g., t(28) = 2.2, p < .05). It recalculates the
    p-value using the reported test statistic and degrees of freedom. If
    the reported and computed p-values don't match, statcheck will flag
    the result as an error. If the reported p-value is statistically
    significant and the recomputed one is not, or vice versa, the result
    will be flagged as a decision error.  You can use statcheck directly
    on a string of text, but you can also scan a PDF or HTML file, or even
    a folder of PDF and/or HTML files.  Statcheck needs an external
    program to convert PDF to text: Xpdf. Instructions on where and how to
    download this program, how to install statcheck, and more details on
    what statcheck can and cannot do can be found in the online manual:
    <https://rpubs.com/michelenuijten/statcheckmanual>.  You can find a
    point-and-click web interface to scan PDF or HTML or DOCX articles on
    <http://statcheck.io>.
	"""
	
	homepage = "https://github.com/MicheleNuijten/statcheck"
	cran = "statcheck" 

	version("1.5.0", md5="b67809f69dba91dca30808f838fdb1bc")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
