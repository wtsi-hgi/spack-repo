# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqdesign(RPackage):
	"""Simulation and Group Sequential Monitoring of Randomized
Two-Stage Treatment Efficacy Trials with Time-to-Event
Endpoints

	A modification of the preventive vaccine efficacy trial design of Gilbert, Grove et al. (2011, Statistical Communications in Infectious Diseases) is implemented, with application generally to individual-randomized clinical trials with multiple active treatment groups and a shared control group, and a study endpoint that is a time-to-event endpoint subject to right-censoring. The design accounts for the issues that the efficacy of the treatment/vaccine groups may take time to accrue while the multiple treatment administrations/vaccinations are given; there is interest in assessing the durability of treatment efficacy over time; and group sequential monitoring of each treatment group for potential harm, non-efficacy/efficacy futility, and high efficacy is warranted. The design divides the trial into two stages of time periods, where each treatment is first evaluated for efficacy in the first stage of follow-up, and, if and only if it shows significant treatment efficacy in stage one, it is evaluated for longer-term durability of efficacy in stage two. The package produces plots and tables describing operating characteristics of a specified design including an unconditional power for intention-to-treat and per-protocol/as-treated analyses; trial duration; probabilities of the different possible trial monitoring outcomes (e.g., stopping early for non-efficacy); unconditional power for comparing treatment efficacies; and distributions of numbers of endpoint events occurring after the treatments/vaccinations are given, useful as input parameters for the design of studies of the association of biomarkers with a clinical outcome (surrogate endpoint problem). The code can be used for a single active treatment versus control design and for a single-stage design.
	"""
	
	homepage = "https://github.com/mjuraska/seqDesign"
	cran = "seqDesign" 

	version("1.2", md5="53a19fbe7f5366e9d0911e34503d63b7")

	depends_on("r@2.16:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
