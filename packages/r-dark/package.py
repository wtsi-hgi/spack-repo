# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDark(RPackage):
	"""The Analysis of Dark Adaptation Data

	The recovery of visual sensitivity in a dark environment is known
    as dark adaptation. In a clinical or research setting the recovery is typically
    measured after a dazzling flash of light and can be described by the Mahroo,
    Lamb and Pugh (MLP) model of dark adaptation. The functions in this package take
    dark adaptation data and use nonlinear regression to find the parameters of the
    model that 'best' describe the data. They do this by firstly, generating rapid
    initial objective estimates of data adaptation parameters, then a multi-start
    algorithm is used to reduce the possibility of a local minimum. There is also a
    bootstrap method to calculate parameter confidence intervals. The functions rely
    upon a 'dark' list or object. This object is created as the first step in the
    workflow and parts of the object are updated as it is processed.
	"""
	
	homepage = "https://github.com/emkayoh/Dark"
	cran = "Dark" 

	version("0.9.8", md5="a917c2d2eeea48cd909dffe8a6060454")

