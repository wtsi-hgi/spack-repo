# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlantecowrap(RPackage):
	"""Enhancing Capabilities of 'plantecophys'

	Provides wrapping functions to add to capabilities to 'plantecophys' 
    (Duursma, 2015, <doi:10.1371/journal.pone.0143346>). Key added capabilities 
    include temperature responses of mesophyll conductance (gm, gmeso), apparent 
    Michaelis-Menten constant for rubisco carboxylation in air (Km, Kcair),and
    photorespiratory CO2 compensation point (GammaStar) for fitting A-Ci or A-Cc
    curves for C3 plants (for temperature responses of gm, Km, & GammaStar,  see 
    Bernacchi et al., 2002, <doi:10.1104/pp.008250>; for theory on fitting A-Ci 
    or A-Cc curves, see Farquhar et al., 1980; <doi:10.1007/BF00386231>, von 
    Caemmerer, 2000, ISBN:064306379X; Ethier & Livingston, 2004 
    <doi:10.1111/j.1365-3040.2004.01140.x>; and Gu et al., 2010, 
    <doi:10.1111/j.1365-3040.2010.02192.x>). Includes the ability to fit the 
    Arrhenius and modified Arrhenius temperature response functions (see Medlyn 
    et al., 2002, <doi:10.1046/j.1365-3040.2002.00891.x>) for maximum rubisco 
    carboxylation rates (Vcmax) and maximum electron transport rates (Jmax) (see
    Farquhar et al., 1980; <doi:10.1007/BF00386231>).
	"""
	
	homepage = "https://github.com/jstinzi/plantecowrap"
	cran = "plantecowrap" 

	version("1.0.4", md5="1c04dfb5a5e25eeaacc475f6beac58d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.1:", type=("build", "run"))
	depends_on("r-plantecophys@1.4.4:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
