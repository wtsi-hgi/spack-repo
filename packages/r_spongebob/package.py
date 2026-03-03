# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpongebob(RPackage):
	"""SpongeBob-Case Converter : spOngEboB-CASe CoNVertER

	Convert text (and text in R objects) to Mocking SpongeBob case 
             <https://knowyourmeme.com/memes/mocking-spongebob> and show them 
             off in fun ways. 
             CoNVErT TexT (AnD TeXt In r ObJeCtS) To MOCkINg SpoNgebOb CAsE
             <https://knowyourmeme.com/memes/mocking-spongebob> aND shOw tHem 
             OFf IN Fun WayS. 
	"""
	
	homepage = "https://github.com/jayqi/spongebob"
	cran = "spongebob" 

	version("0.4.0", md5="a1975481bc55b6153e1890bb3d106067")

