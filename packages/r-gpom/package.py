# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpom(RPackage):
	"""Generalized Polynomial Modelling

	Platform dedicated to the Global Modelling technique. Its aim
    is to obtain ordinary differential equations of polynomial form directly
    from time series. It can be applied to single or multiple time series under
    various conditions of noise, time series lengths, sampling, etc. This platform
    is developped at the Centre d'Etudes Spatiales de la Biosphere (CESBIO),
    UMR 5126 UPS/CNRS/CNES/IRD, 18 av. Edouard Belin, 31401 TOULOUSE, FRANCE.
    The developments were funded by the French program Les Enveloppes Fluides
    et l'Environnement (LEFE, MANU, projets GloMo, SpatioGloMo and MoMu). The
    French program Defi InFiNiTi (CNRS) and PNTS are also acknowledged (projects
    Crops'IChaos and Musc & SlowFast). The method is described in the article :
    Mangiarotti S. and Huc M. (2019) <doi:10.1063/1.5081448>.
	"""
	
	cran = "GPoM" 

	version("1.4", md5="4f0d17ea86c79df24a993cb0c790ed54")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-float", type=("build", "run"))
