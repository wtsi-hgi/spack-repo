# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReclin2(RPackage):
	"""Record Linkage Toolkit

	Functions to assist in performing probabilistic record linkage and
    deduplication: generating pairs, comparing records, em-algorithm for
    estimating m- and u-probabilities
    (I. Fellegi & A. Sunter (1969) <doi:10.1080/01621459.1969.10501049>, 
    T.N. Herzog, F.J. Scheuren, & W.E. Winkler (2007), 
    "Data Quality and Record Linkage Techniques", ISBN:978-0-387-69502-0),
    forcing one-to-one matching. Can also be
    used for pre- and post-processing for machine learning methods for record
    linkage. Focus is on memory, CPU performance and flexibility. 
	"""
	
	homepage = "https://github.com/djvanderlaan/reclin2"
	cran = "reclin2" 

	version("0.5.0", md5="5fcceed79f53cd9a0b5da34db17262a6", url="https://cran.r-project.org/src/contrib/reclin2_0.5.0.tar.gz")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
