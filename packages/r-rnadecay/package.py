# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnadecay(RPackage):
	"""Maximum Likelihood Decay Modeling of RNA Degradation Data

	RNA degradation is monitored through measurement of RNA abundance after inhibiting RNA synthesis. This package has functions and example scripts to facilitate (1) data normalization, (2) data modeling using constant decay rate or time-dependent decay rate models, (3) the evaluation of treatment or genotype effects, and (4) plotting of the data and models. Data Normalization: functions and scripts make easy the normalization to the initial (T0) RNA abundance, as well as a method to correct for artificial inflation of Reads per Million (RPM) abundance in global assessments as the total size of the RNA pool decreases. Modeling: Normalized data is then modeled using maximum likelihood to fit parameters. For making treatment or genotype comparisons (up to four), the modeling step models all possible treatment effects on each gene by repeating the modeling with constraints on the model parameters (i.e., the decay rate of treatments A and B are modeled once with them being equal and again allowing them to both vary independently). Model Selection: The AICc value is calculated for each model, and the model with the lowest AICc is chosen. Modeling results of selected models are then compiled into a single data frame. Graphical Plotting: functions are provided to easily visualize decay data model, or half-life distributions using ggplot2 package functions.
	"""
	
	bioc = "RNAdecay" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNAdecay_1.22.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNAdecay/RNAdecay_1.22.2.tar.gz"]

	version("1.22.2", sha256="c7ee3059b07ee28c2814ee9104e02259f5c53681cf04de9a311bc81a82c0ebdb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
