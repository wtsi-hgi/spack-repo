# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManta(RPackage):
	"""Multivariate Asymptotic Non-Parametric Test of Association

	The Multivariate Asymptotic Non-parametric Test of Association (MANTA) enables 
    non-parametric, asymptotic P-value computation for multivariate linear models. MANTA
    relies on the asymptotic null distribution of the PERMANOVA test statistic. P-values are
    computed using a highly accurate approximation of the corresponding cumulative distribution 
    function. Garrido-Martín et al. (2022) <doi:10.1101/2022.06.06.493041>.
	"""
	
	homepage = "https://github.com/dgarrimar/manta"
	cran = "manta" 

	version("1.0.1", md5="0338dbc6a837583ab86724bf3eb481f6")

	depends_on("r@3.3.2:", type=("build", "run"))
