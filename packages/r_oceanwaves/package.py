# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROceanwaves(RPackage):
	"""Ocean Wave Statistics

	Calculate ocean wave height summary statistics and process data 
    from bottom-mounted pressure sensor data loggers. Derived primarily from 
    MATLAB functions provided by U. Neumeier at 
    <http://neumeier.perso.ch/matlab/waves.html>. Wave number 
    calculation based on the algorithm in Hunt, J. N. (1979, ISSN:0148-9895) 
    "Direct Solution of Wave Dispersion Equation", American Society of Civil 
    Engineers Journal of the Waterway, Port, Coastal, and Ocean Division, 
    Vol 105, pp 457-459.
	"""
	
	homepage = "https://github.com/millerlp/oceanwaves"
	cran = "oceanwaves" 

	version("0.2.0", md5="04283ffdbb69addf3dafa4f9eaee930c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bspec", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
