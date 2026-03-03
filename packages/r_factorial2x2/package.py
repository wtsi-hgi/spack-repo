# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactorial2x2(RPackage):
	"""Design and Analysis of a 2x2 Factorial Trial

	Used for the design and analysis of a 2x2 factorial trial for
    a time-to-event endpoint.  It performs power calculations and significance
    testing as well as providing estimates of the relevant hazard ratios and the 
    corresponding 95% confidence intervals.  Important reference papers include
    Slud EV. (1994) <https://www.ncbi.nlm.nih.gov/pubmed/8086609>
    Lin DY, Gong J, Gallo P, Bunn PH, Couper D. (2016) <DOI:10.1111/biom.12507>
    Leifer ES, Troendle JF, Kolecki A, Follmann DA. (2020)
    <https://github.com/EricSLeifer/factorial2x2/blob/master/Leifer%20et%20al.%20paper.pdf>.
	"""
	
	cran = "factorial2x2" 

	version("0.2.0", md5="9579ae80c62a748799a521c09491b8c6", url="https://cran.r-project.org/src/contrib/factorial2x2_0.2.0.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
