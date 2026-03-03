# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPksensi(RPackage):
	"""Global Sensitivity Analysis in Physiologically Based Kinetic
Modeling

	Applying the global sensitivity analysis workflow to investigate 
    the parameter uncertainty and sensitivity in physiologically based 
    kinetic (PK) models, especially the physiologically based 
    pharmacokinetic/toxicokinetic model with multivariate outputs. 
    The package also provides some functions to check the convergence 
    and sensitivity of model parameters. The workflow was first mentioned 
    in Hsieh et al., (2018) <doi:10.3389/fphar.2018.00588>, then further 
    refined (Hsieh et al., 2020 <doi:10.1016/j.softx.2020.100609>).                
	"""
	
	homepage = "https://github.com/nanhung/pksensi"
	cran = "pksensi" 

	version("1.2.3", md5="88c979f62a65056a33f71c161fe9112c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
