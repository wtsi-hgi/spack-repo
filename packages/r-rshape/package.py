# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRshape(RPackage):
	"""Simulated Haploid Asexual Population Evolution

	In silico experimental evolution offers a cost-and-time effective means to test evolutionary hypotheses.  Existing evolutionary simulation tools focus on simulations in a limited experimental framework, and tend to report on only the results presumed of interest by the tools designer.  The R-package for Simulated Haploid Asexual Population Evolution ('rSHAPE') addresses these concerns by implementing a robust simulation framework that outputs complete population demographic and genomic information for in silico evolving communities.  Allowing more than 60 parameters to be specified, 'rSHAPE'	simulates evolution across discrete time-steps for an evolving community of haploid asexual populations with binary state genomes.  These settings are for the current state of 'rSHAPE' and future steps will be to increase the breadth of evolutionary conditions permitted.  At present, most effort was placed into permitting varied growth models to be simulated (such as constant size, exponential growth, and logistic growth) as well as various fitness landscape models to reflect the evolutionary landscape (e.g.: Additive, House of Cards - Stuart Kauffman and Simon Levin (1987) <doi:10.1016/S0022-5193(87)80029-2>, NK - Stuart A. Kauffman and Edward D. Weinberger (1989) <doi:10.1016/S0022-5193(89)80019-0>, Rough Mount Fuji - Neidhart, Johannes and Szendro, Ivan G and Krug, Joachim (2014) <doi:10.1534/genetics.114.167668>). This package includes numerous functions though users will only need defineSHAPE(), runSHAPE(), shapeExperiment() and summariseExperiment().  All other functions are called by these main functions and are likely only to be on interest for someone wishing to develop 'rSHAPE'.  Simulation results will be stored in files which are exported to the directory referenced by the shape_workDir option (defaults to tempdir() but do change this by passing a folderpath argument for workDir when calling defineSHAPE() if you plan to make use of your results beyond your current session).  'rSHAPE' will generate numerous replicate simulations for your defined range of experimental parameters.  The experiment will be built under the experimental working directory (i.e.: referenced by the option shape_workDir set using defineSHAPE() ) where individual replicate simulation results will be stored as well as processed results which I have made in an effort to facilitate analyses by automating collection and processing of the potentially thousands of files which will be created. On that note, 'rSHAPE' implements a robust and flexible framework with highly detailed output at the cost of computational efficiency and potentially requiring significant disk space (generally gigabytes but up to tera-bytes for very large simulation efforts).  So, while 'rSHAPE' offers a single framework in which we can simulate evolution and directly compare the impacts of a wide range of parameters, it is not as quick to run as other in silico simulation tools which focus on a single scenario with limited output. There you have it, 'rSHAPE' offers you a less restrictive in silico evolutionary playground than other tools and I hope you enjoy testing your hypotheses.
	"""
	
	cran = "rSHAPE" 

	version("0.3.2", md5="53aee95996459db6bc18f5aac948f39c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
