# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBi(RPackage):
	"""Blinding Assessment Indexes for Randomized, Controlled, Clinical
Trials

	Generate the James Blinding Index, as described in James et al (1996) 
             <https://pubmed.ncbi.nlm.nih.gov/8841652/> and the Bang Blinding Index, 
             as described in Bang et al (2004) <https://pubmed.ncbi.nlm.nih.gov/15020033/>.
             These are measures to assess whether or not satisfactory blinding has been 
             maintained in a randomized, controlled, clinical trial. These can be generated 
             for trial subjects, research coordinators and principal investigators, based 
             upon standardized questionnaires that have been administered, to assess whether
             or not they can correctly guess to which treatment arm (e.g. placebo or treatment) 
             subjects were assigned at randomization. 
	"""
	
	homepage = "https://github.com/marcschwartz/BI"
	cran = "BI" 

	version("1.2.0", md5="b95d715a19a60b1de77b436de085cd36")

