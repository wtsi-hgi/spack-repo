# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPro(RPackage):
	"""Point-Process Response Model for Optogenetics

	Optogenetics is a new tool to study neuronal circuits that have been genetically modified to allow stimulation by flashes of light.  This package implements the methodological framework, Point-process Response model for Optogenetics (PRO), for analyzing data from these experiments.  This method provides explicit nonlinear transformations to link the flash point-process with the spiking point-process.  Such response functions can be used to provide important and interpretable scientific insights into the properties of the biophysical process that governs neural spiking in response to optogenetic stimulation.
	"""
	
	cran = "pro" 

	version("0.1.1", md5="e0ebbbbbafe4948cf3cada1b199f25bb")

