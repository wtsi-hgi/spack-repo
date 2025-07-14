# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicdatalymphoblast(RPackage):
	"""Human lymphoblastoid HiC data from Lieberman-Aiden et al. 2009

	The HiC data from human lymphoblastoid cell line (HindIII restriction) was retrieved from the sequence read archive and two ends of the paired reads were aligned separately with bowtie.
	"""
	
	bioc = "HiCDataLymphoblast"

	version("1.44.0", commit="76b1851a21b45e99fe65bbbb800f2c75e14a4aab")
	version("1.38.0", commit="ea46ff5adec3d70e1f061baf5653c7a3b1cc8711")


