# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCotima(RPackage):
	"""Continuous Time Meta-Analysis ('CoTiMA')

	The 'CoTiMA' package performs meta-analyses of correlation matrices of repeatedly measured variables taken from 
   studies that used different time intervals. Different time intervals between measurement occasions impose problems for 
   meta-analyses because the effects (e.g. cross-lagged effects) cannot be simply aggregated, for example, by means of common 
   fixed or random effects analysis. However, continuous time math, which is applied in 'CoTiMA', can be used to extrapolate or 
   intrapolate the results from all studies to any desired time lag. By this, effects obtained in studies that used different 
   time intervals can be meta-analyzed. 'CoTiMA' fits models to empirical data using the structural equation model (SEM) package 
   'ctsem', the effects specified in a SEM are related to parameters that are not directly included in the model (i.e., 
   continuous time parameters; together, they represent the continuous time structural equation model, CTSEM). Statistical 
   model comparisons and significance tests are then performed on the continuous time parameter estimates. 'CoTiMA' also allows 
   analysis of publication bias (Egger's test, PET-PEESE estimates, zcurve analysis etc.) and analysis of statistical power 
   (post hoc power, required sample sizes). See Dormann, C., Guthier, C., & Cortina, J. M. (2019) <doi:10.1177/1094428119847277>.
   and Guthier, C., Dormann, C., & Voelkle, M. C. (2020) <doi:10.1037/bul0000304>.
	"""
	
	homepage = "https://github.com/CoTiMA/CoTiMA"
	cran = "CoTiMA" 

	version("0.7.0", md5="7160a7fb57658d1e048833897cc23ecf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-openmx@2.18.1:", type=("build", "run"))
	depends_on("r-ctsem@3.8.1:", type=("build", "run"))
	depends_on("r-lavaan@0.6:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-mbess@4.6:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-psych@1.9.12:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
	depends_on("r-rootsolve@1.8.2:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-rpushbullet@0.3.3:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.2:", type=("build", "run"))
	depends_on("r-zcurve@1.0.7:", type=("build", "run"))
	depends_on("r-scholar@0.2:", type=("build", "run"))
	depends_on("r-stringi@1.0.7:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
