# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWals(RPackage):
	"""Weighted-Average Least Squares Model Averaging

	Implements Weighted-Average Least Squares model averaging
    for negative binomial regression models of Huynh (2023) (mimeo),
    generalized linear models of De Luca, Magnus, Peracchi (2018) 
    <doi:10.1016/j.jeconom.2017.12.007> and linear regression models of 
    Magnus, Powell, Pruefer (2010) <doi:10.1016/j.jeconom.2009.07.004>, see also 
    Magnus, De Luca (2016) <doi:10.1111/joes.12094>. Weighted-Average Least Squares
    for the linear regression model is based on the original 'MATLAB' code by 
    Magnus and De Luca <https://www.janmagnus.nl/items/WALS.pdf>, see also 
    Kumar, Magnus (2013) <doi:10.1007/s13571-013-0060-9> and 
    De Luca, Magnus (2011) <doi:10.1177/1536867X1201100402>.
	"""
	
	homepage = "https://github.com/kevhuy/WALS"
	cran = "WALS" 

	version("0.2.4", md5="ae171be6f84b80f5cfa02ea4cd2045c0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-formula@1.2.3:", type=("build", "run"))
	depends_on("r-mass@7.3.51.6:", type=("build", "run"))
	depends_on("r-rdpack@2.1.3:", type=("build", "run"))
