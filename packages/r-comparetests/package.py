# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparetests(RPackage):
	"""Correct for Verification Bias in Diagnostic Accuracy & Agreement

	A standard test is observed on all specimens.  We treat the second test (or sampled test) as being conducted on only a stratified sample of specimens.  Verification Bias is this situation when the specimens for doing the second (sampled) test is not under investigator control.  We treat the total sample as stratified two-phase sampling and use inverse probability weighting.  We estimate diagnostic accuracy (category-specific classification probabilities; for binary tests reduces to specificity and sensitivity, and also predictive values) and agreement statistics (percent agreement, percent agreement by category, Kappa (unweighted), Kappa (quadratic weighted) and symmetry tests (reduces to McNemar's test for binary tests)).  See: Katki HA, Li Y, Edelstein DW, Castle PE.  Estimating the agreement and diagnostic accuracy of two diagnostic tests when one test is conducted on only a subsample of specimens. Stat Med. 2012 Feb 28; 31(5) <doi:10.1002/sim.4422>.
	"""
	
	homepage = "http://dceg.cancer.gov/about/staff-directory/biographies/A-J/katki-hormuzd"
	cran = "CompareTests" 

	version("1.2", md5="0a55bc17f788c176428b3f6e0cd3dfed")

