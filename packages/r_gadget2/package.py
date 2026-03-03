# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGadget2(RPackage):
	"""Gadget is the Globally-Applicable Area Disaggregated General
Ecosystem Toolbox

	A statistical ecosystem modelling package, taking many features of
             the ecosystem into account. Gadget works by running an internal
             model based on many parameters, and then comparing the data from
             the output of this model to real data to get a goodness-of-fit
             likelihood score. These parameters can then be adjusted, and the
             model re-run, until an optimum is found, which corresponds to the
             model with the lowest likelihood score. Gadget allows the user to
             include a number of features into an ecosystem model: One or more
             species, each of which may be split into multiple stocks; multiple
             areas with migration between areas; predation between and within
             species; maturation; reproduction and recruitment; multiple
             commercial and survey fleets taking catches from the populations.
             For more details see <https://gadget-framework.github.io/gadget2/>.
             This is the C++ Gadget2 runtime, making it available for R.
	"""
	
	cran = "gadget2" 

	version("2.3.11", md5="439fbb4050d6be4a57bd4c5f30af0959", url="https://cran.r-project.org/src/contrib/gadget2_2.3.11.tar.gz")

