# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcr(RPackage):
	"""Quality Control Review

	Univariate and multivariate SQC tools that completes and increases
    the SQC techniques available in R. Apart from integrating different R packages 
    devoted to SQC ('qcc','MSQC'), provides nonparametric tools that are highly 
    useful when Gaussian assumption is not met. 
    This package computes standard univariate control charts for individual measurements, 
    'X-bar', 'S', 'R', 'p', 'np', 'c', 'u', 'EWMA' and 'CUSUM'. In addition, it 
    includes functions to perform multivariate control charts such as 'Hotelling T2', 
    'MEWMA' and 'MCUSUM'. As representative feature, multivariate nonparametric 
    alternatives based on data depth are implemented in this package: 'r', 'Q' and 
    'S' control charts. In addition, Phase I and II control charts for functional 
    data are included. This package also allows the estimation of the most complete 
    set of capability indices from first to fourth generation, covering the nonparametric 
    alternatives, and performing the corresponding capability analysis graphical outputs,
    including the process capability plots. See Flores et al. (2021) <doi:10.32614/RJ-2021-034>.
	"""
	
	homepage = "https://github.com/mflores72000/qcr"
	cran = "qcr" 

	version("1.4", md5="e857afe78c9b259b56336b76a9cf29d6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-qcc", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
