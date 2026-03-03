# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRspincalc(RPackage):
	"""Conversion Between Attitude Representations of DCM, Euler
Angles, Quaternions, and Euler Vectors

	Conversion between attitude representations: DCM, Euler angles, Quaternions, and Euler vectors.
    Plus conversion between 2 Euler angle set types (xyx, yzy, zxz, xzx, yxy, zyz, xyz, yzx, zxy, xzy, yxz, zyx).
    Fully vectorized code, with warnings/errors for Euler angles (singularity, out of range, invalid angle order), 
    DCM (orthogonality, not proper, exceeded tolerance to unity determinant) and Euler vectors(not unity).
    Also quaternion and other useful functions.
    Based on SpinCalc by John Fuller and SpinConv by Paolo de Leva.
	"""
	
	cran = "RSpincalc" 

	version("1.0.2", md5="46901af3d98dc3e7247b39371d5320bf")

