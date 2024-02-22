# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrepdesigns(RPackage):
	"""Partially Replicated (p-Rep) Designs

	Early generation breeding trials are to be conducted in multiple 
             environments where it may not be possible to replicate all the 
             lines in each environment due to scarcity of resources. For such 
             situations, partially replicated (p-Rep) designs have wide 
             application potential as only a proportion of the test lines are 
             replicated at each environment. A collection of several utility 
             functions related to p-Rep designs have been developed. Here, the 
             package contains six functions for a complete stepwise analytical 
             study of these designs. Five functions pRep1(), pRep2(), pRep3(), 
             pRep4() and pRep5(), are used to generate five new series of p-Rep 
             designs and also compute average variance factors and canonical 
             efficiency factors of generated designs. A fourth function NCEV() 
             is used to generate incidence matrix (N), information matrix (C), 
             canonical efficiency factor (E) and average variance factor (V). 
             This function is general in nature and can be used for studying the 
             characterization properties of any block design. A construction 
             procedure for p-Rep designs was given by Williams et al.(2011) 
             <doi:10.1002/bimj.201000102> which was tedious and time consuming. 
             Here, in this package, five different methods have been given to 
             generate p-Rep designs easily.
	"""
	
	cran = "pRepDesigns" 

	version("1.1.0", md5="52d34a433fac9db96435cef7107ff4aa")

