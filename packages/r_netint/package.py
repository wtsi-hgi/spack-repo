# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetint(RPackage):
	"""Methods for Unweighted and Weighted Network Integration

	Implementation of network integration approaches
    comprising unweighted and weighted integration methods. Unweighted integration
    is performed considering the average, per-edge average, maximum and minimum of
    networks edges. Weighted integration takes into account a weight for each 
    network during the fusion process, where the weights express
    the ''predictiveness strength'' of each network considering a specific predictive
    task. Weights can be learned using a machine learning algorithm able to associate
    the weights to the assessment of the accuracy of the learning algorithm 
    trained on the network itself. The implemented methods can be applied to 
    effectively integrate different biological networks modelling a wide range
    of problems in bioinformatics (e.g. disease gene prioritization, protein
    function prediction, drug repurposing, clinical outcome prediction).
	"""
	
	cran = "NetInt" 

	version("1.0.0", md5="5392d13a15f87b249d16b75667945f39")

	depends_on("r-mathjaxr", type=("build", "run"))
