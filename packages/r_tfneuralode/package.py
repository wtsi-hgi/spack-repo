# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfneuralode(RPackage):
	"""Create Neural Ordinary Differential Equations with 'tensorflow'

	Provides a framework for the creation and use of Neural ordinary
    differential equations with the 'tensorflow' and 'keras' packages. 
    The idea of Neural ordinary differential equations comes from 
    Chen et al. (2018) <doi:10.48550/arXiv.1806.07366>, and 
    presents a novel way of learning and solving differential systems. 
	"""
	
	homepage = "https://github.com/semran9/tfNeuralODE"
	cran = "tfNeuralODE" 

	version("0.1.0", md5="13197c2ce9a29425245a4bcd3d214af2")

	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
