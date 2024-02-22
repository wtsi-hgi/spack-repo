# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHightr(RPackage):
	"""HIGHT Algorithm

	HIGHT(HIGh security and light weigHT) algorithm is a block cipher encryption algorithm developed to provide confidentiality in computing environments that demand low power consumption and lightweight, such as RFID(Radio-Frequency Identification) and USN(Ubiquitous Sensor Network), or in mobile environments that require low power consumption and lightweight, such as smartphones and smart cards. Additionally, it is designed with a simple structure that enables it to be used with basic arithmetic operations, XOR, and circular shifts in 8-bit units. This algorithm was designed to consider both safety and efficiency in a very simple structure suitable for limited environments, compared to the former 128-bit encryption algorithm SEED. In December 2010, it became an ISO(International Organization for Standardization) standard. The detailed procedure is described in Hong et al. (2006) <doi:10.1007/11894063_4>.
	"""
	
	homepage = "https://github.com/Yongwoo-Eg-Kim/hightR"
	cran = "hightR" 

	version("0.3.0", md5="1338db33a9ec2902d72f511010bc4ffc")

