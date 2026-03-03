# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegmag(RPackage):
	"""Determine Event Boundaries in Event Segmentation Experiments

	Contains functions that help to determine event
    boundaries in event segmentation experiments by bootstrapping a critical
    segmentation magnitude under the null hypothesis that all key presses were
    randomly distributed across the experiment. Segmentation magnitude is
    defined as the sum of Gaussians centered at the times of the segmentation
    key presses performed by the participants. Within a participant, the maximum
    of the overlaid Gaussians is used to prevent an excessive influence of a
    single participant on the overall outcome (e.g. if a participant is pressing
    the key multiple times in succession). Further functions are included, such
    as plotting the results.
	"""
	
	cran = "segmag" 

	version("1.2.4", md5="74d98e64c995e6fd309a50ab36df5b6a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
