# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmas(RPackage):
	"""Epigenome-Wide Mediation Analysis Study

	DNA methylation is essential for human, and environment can change the DNA methylation
    and affect body status. Epigenome-Wide Mediation Analysis Study (EMAS) can find
    potential mediator CpG sites between exposure (x) and outcome (y) in epigenome-wide.
    For more information on the methods we used, please see the following references:
    Tingley, D. (2014) <doi:10.18637/jss.v059.i05>,
    Turner, S. D. (2018) <doi:10.21105/joss.00731>,
    Rosseel, D. (2012) <doi:10.18637/jss.v048.i02>.
	"""
	
	cran = "EMAS" 

	version("0.2.2", md5="b48f0975bdc7298a38205a7dd094c0c5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mediation", type=("build", "run"))
	depends_on("r-multilevel", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicanno-ilm10b4-hg19", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
