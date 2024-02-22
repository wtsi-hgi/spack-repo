# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapena(RPackage):
	"""M-Estimation of Shape for Data with Missing Values

	M-estimators of location and shape following the power family 
    (Frahm, Nordhausen, Oja (2020) <doi:10.1016/j.jmva.2019.104569>) are 
    provided in the case of complete data and also when observations have 
    missing values together with functions aiding their visualization.
	"""
	
	cran = "shapeNA" 

	version("0.0.2", md5="d9efd30ad4422cac69d7bd4ce46cdefb")

	depends_on("r@3.6:", type=("build", "run"))
