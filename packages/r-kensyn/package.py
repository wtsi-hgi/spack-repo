# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKensyn(RPackage):
	"""Knowledge Synthesis in Agriculture - From Experimental Network
to Meta-Analysis

	Demo and dataset accompaying the books :
	De l'analyse des réseaux expérimentaux à la méta-analyse: Méthodes et applications avec le logiciel R pour les sciences agronomiques et environnementales (Published 2018-06-28, Quae, for french version) by David Makowski, Francois Piraux and Francois Brun - <https://www.quae.com/produit/1514/9782759228164/de-l-analyse-des-reseaux-experimentaux-a-la-meta-analyse>
	Knowledge Synthesis in Agriculture : from Experimental Network to Meta-Analysis (in preparation for 2018-06, Springer , for English version) by David Makowski, Francois Piraux and Francois Brun
	A full description of all the material is in both books.
	ACKNOWLEDGMENTS : The French network "RMT modeling and data analysis for agriculture" (<http://www.modelia.org>) have contributed to the development of this R package. This project and network are lead by ACTA (French Technical Institute for Agriculture) and was funded by a grant from the Ministry of Agriculture and Fishing of France.
	"""
	
	homepage = "http://www.modelia.org"
	cran = "KenSyn" 

	version("0.3", md5="9f89c7b9983126234a620e543ee00dc7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
