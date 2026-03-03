# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdn(RPackage):
	"""Personalized Disease Network

	Building patient level networks for prediction of 
        medical outcomes and draw the cluster of network.        
        This package is based on paper Personalized disease 
        networks for understanding and predicting cardiovascular 
        diseases and other complex processes 
        (See Cabrera et al. <http://circ.ahajournals.org/content/134/Suppl_1/A14957>).
	"""
	
	cran = "PDN" 

	version("0.1.0", md5="ae8fd3974172526938889f7a08dc6e62")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
