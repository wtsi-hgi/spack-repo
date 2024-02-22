# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbm(RPackage):
	"""Agent Based Model Simulation Framework

	A high-performance, flexible and extensible framework to
    develop continuous-time agent based models. Its high performance
    allows it to simulate millions of agents efficiently. Agents are
    defined by their states (arbitrary R lists). The events are handled in
    chronological order. This avoids the multi-event interaction problem
    in a time step of discrete-time simulations, and gives precise
    outcomes. The states are modified by provided or user-defined events.
    The framework provides a flexible and customizable implementation of
    state transitions (either spontaneous or caused by agent
    interactions), making the framework suitable to apply to epidemiology
    and ecology, e.g., to model life history stages, competition and
    cooperation, and disease and information spread. The agent
    interactions are flexible and extensible. The framework provides
    random mixing and network interactions, and supports multi-level
    mixing patterns.  It can be easily extended to other interactions such
    as inter- and intra-households (or workplaces and schools) by
    subclassing an R6 class. It can be used to study the effect of
    age-specific, group-specific, and contact- specific intervention
    strategies, and complex interactions between individual behavior and
    population dynamics. This modeling concept can also be used in
    business, economical and political models. As a generic event based
    framework, it can be applied to many other fields. More information
    about the implementation and examples can be found at
    <https://github.com/junlingm/ABM>.
	"""
	
	homepage = "https://github.com/junlingm/ABM"
	cran = "ABM" 

	version("0.3", md5="3a4aa189210b83d44e04f3a96f3112a0")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
