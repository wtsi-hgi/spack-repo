# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhagecocktail(RPackage):
	"""Design of the Best Phage Cocktail

	There are 4 possible methods: "ExhaustiveSearch"; "ExhaustivePhi";    "ClusteringSearch"; and "ClusteringPhi". 
    "ExhaustiveSearch"--> gives you the best phage cocktail from a phage-bacteria
	infection network. It checks different phage cocktail sizes from 1 to 7 and
	only stops before if it lyses all bacteria. Other option is when users have
	decided not to obtain a phage cocktail size higher than a limit value.
    "ExhaustivePhi"--> firstly, it finds Phi out. Phi is a formula
	indicating the necessary phage cocktail size. Phi needs nestedness temperature
	and fill, which are internally calculated. This function will only look for the
	best combination (phage cocktail) with a Phi size.
    "ClusteringSearch"--> firstly, an agglomerative hierarchical clustering using
	Ward's algorithm is calculated for phages. They will be clustered according to
	bacteria lysed by them. PhageCocktail() chooses how many clusters are needed in
	order to select 1 phage per cluster. Using the phages selected during the
	clustering, it checks different phage cocktail sizes from 1 to 7 and only stops
	before if it lyses all bacteria. Other option is when users have decided not to
	obtain a phage cocktail size higher than a limit value.
    "ClusteringPhi"--> firstly, an agglomerative hierarchical clustering using Ward's
	algorithm is calculated for phages. They will be clustered according to bacteria
	lysed by them. PhageCocktail() chooses how many clusters are needed in order to
	select 1 phage per cluster. Once the function has one phage per cluster, it
	calculates Phi. If the number of clusters is less than Phi number, it will be
	changed to obtain, as minimum, this quantity of candidates (phages). Then, it
	calculates the best combination of Phi phages using those selected during the
	clustering with Ward algorithm.
	  If you use PhageCocktail, please cite it as:
  "PhageCocktail: An R Package to Design Phage Cocktails from Experimental 
  Phage-Bacteria Infection Networks". María Victoria Díaz-Galián, Miguel A. 
  Vega-Rodríguez, Felipe Molina. Computer Methods and Programs in Biomedicine,
  221, 106865, Elsevier Ireland, Clare, Ireland, 2022, pp. 1-9, ISSN: 0169-2607.
  <doi:10.1016/j.cmpb.2022.106865>.
	"""
	
	cran = "PhageCocktail" 

	version("1.0.3", md5="b323426fa510fb5a4e20bd1c890dd04c")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-smerc", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
