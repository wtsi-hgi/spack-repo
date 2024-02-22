# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotosynthesis(RPackage):
	"""Tools for Plant Ecophysiology & Modeling

	Contains modeling and analytical tools for plant ecophysiology.
    MODELING: Simulate C3 photosynthesis using the Farquhar, von Caemmerer,
    Berry (1980) <doi:10.1007/BF00386231> model as described in Buckley and
    Diaz-Espejo (2015) <doi:10.1111/pce.12459>. It uses units to ensure that
    parameters are properly specified and transformed before calculations.
    Temperature response functions get automatically "baked" into all
    parameters based on leaf temperature following Bernacchi et al. (2002)
    <doi:10.1104/pp.008250>. The package includes boundary layer, cuticular,
    stomatal, and mesophyll conductances to CO2, which each can vary on the
    upper and lower portions of the leaf. Use straightforward functions to
    simulate photosynthesis over environmental gradients such as Photosynthetic
    Photon Flux Density (PPFD) and leaf temperature, or over trait gradients
    such as CO2 conductance or photochemistry. 
    ANALYTICAL TOOLS: Fit ACi (Farquhar et al. (1980) <doi:10.1007/BF00386231>)
    and AQ curves (Marshall & Biscoe (1980) <doi:10.1093/jxb/31.1.29>),
    temperature responses (Heskel et al. (2016) <doi:10.1073/pnas.1520282113>;
    Kruse et al. (2008) <doi:10.1111/j.1365-3040.2008.01809.x>, Medlyn et al.
    (2002) <doi:10.1046/j.1365-3040.2002.00891.x>, Hobbs et al. (2013)
    <doi:10.1021/cb4005029>), respiration in the light (Kok (1956)
    <doi:10.1016/0006-3002(56)90003-8>, Walker & Ort (2015) <doi:10.1111/pce.12562>,
    Yin et al. (2009) <doi:10.1111/j.1365-3040.2009.01934.x>, Yin et al. (2011)
    <doi:10.1093/jxb/err038>), mesophyll conductance (Harley et al. (1992)
    <doi:10.1104/pp.98.4.1429>), pressure-volume curves (Koide et al. (2000)
    <doi:10.1007/978-94-009-2221-1_9>, Sack et al. (2003)
    <doi:10.1046/j.0016-8025.2003.01058.x>, Tyree et al. (1972)
    <doi:10.1093/jxb/23.1.267>), hydraulic vulnerability curves (Ogle et al. (2009)
    <doi:10.1111/j.1469-8137.2008.02760.x>, Pammenter et al. (1998)
    <doi:10.1093/treephys/18.8-9.589>), and tools for running sensitivity
    analyses particularly for variables with uncertainty (e.g. g_mc(), gamma_star(),
    R_d()).
	"""
	
	homepage = "https://github.com/cdmuir/photosynthesis"
	cran = "photosynthesis" 

	version("2.1.4", md5="aebd39a5e45361126b0bc8bc10e09e51")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.1:", type=("build", "run"))
	depends_on("r-units@0.6.6:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-furrr@0.1:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-gunit@1.0.2:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-nlme@3.1.147:", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tealeaves@1.0.5:", type=("build", "run"))
