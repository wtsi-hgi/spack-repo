# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlantphysior(RPackage):
	"""Fundamental Formulas for Plant Physiology

	Functions tailored for scientific and student communities involved in plant science research. Functionalities encompass estimation chlorophyll content according to Arnon (1949) <doi:10.1104/pp.24.1.1>, determination water potential of Polyethylene glycol(PEG)6000 as in Michel and Kaufmann (1973) <doi:10.1104/pp.51.5.914>  and functions related to estimation of yield related indices like Abiotic tolerance index as given by Moosavi et al.(2008)<doi:10.22059/JDESERT.2008.27115>, Geometric mean productivity (GMP) by Fernandez (1992) <ISBN:92-9058-081-X>, Golden Mean by Moradi et al.(2012)<doi:10.14207/ejsd.2012.v1n3p543>, HAM by Schneider et al.(1997)<doi:10.2135/cropsci1997.0011183X003700010007x>,MPI and TOL by Hossain etal., (1990)<doi:10.2135/cropsci1990.0011183X003000030030x>, RDI by Fischer et al. (1979)<doi:10.1071/AR9791001>,SSI by Fisher et al.(1978)<doi:10.1071/AR9780897>, STI by Fernandez (1993)<doi:10.22001/wvc.72511>,YSI by Bouslama & Schapaugh (1984)<doi:10.2135/cropsci1984.0011183X002400050026x>, Yield index by Gavuzzi et al.(1997)<doi:10.4141/P96-130>. 
	"""
	
	homepage = "https://github.com/rameshram96/plantphysioR"
	cran = "plantphysioR" 

	version("1.0.0", md5="1d02364fdf3861217f38a5150a03217e")

	depends_on("r@2.10:", type=("build", "run"))
