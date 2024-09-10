# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyImutils(PythonPackage):
	"""A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3."""
	
	homepage = "https://github.com/jrosebr1/imutils"
	pypi = "imutils/imutils-0.5.4.tar.gz" 

	version("0.1", sha256="507054891a88c6d8ae6aec1d615ecced04f63fd456ad5b1c7a919e2bcc85a7e3")
	version("0.2", sha256="f5b57b4199d7fa3089dda16bc51ec390736b4fb86dced4cadcbe86e5ce9cb980")
	version("0.2.1", sha256="ba1406206babd7f11bee3850da74bd509c89b8e5918b056e5345964271c01cc8")
	version("0.2.2", sha256="0e50967ac314da97f92296841dfbc76962c531f1d1b894136c3c14d36b7efca8")
	version("0.2.3", sha256="708fdebf93594af2c94c8bf62978d447d04b04ad9a610ca7898b21f8af81bbe9")
	version("0.2.4", sha256="e902f5a6c6db047e76b7705dd112c3fba820879bca07d75e32bdc2d70ccabd22")
	version("0.3", sha256="86806683ea1fa934d15a86edfa9b8fa0b8113d686a0a27ccf271d221f2fe68ca")
	version("0.3.1", sha256="508a9e83b9a37c9e2cb4fe0dafad5bd130f9e0f44adbd588df98a252a752cbcb")
	version("0.3.10", sha256="f6d3354290e9225d09ab53b19c903ca6b5a82115ebfa5c5fd171aa973927471d")
	version("0.3.2", sha256="c16072350b478b98b915251d0a011e36e793cefad92a63a428a2f220eb57a2e9")
	version("0.3.3", sha256="362048c945d45e590245b1ba4ac28f6efa0aaa820ecaccbc74e44aa5f6dff689")
	version("0.3.4", sha256="a617ebc7c880a38dbe2b16049a452b2161f43697e43f3ee6fd70e2c5eb67a8a9")
	version("0.3.5", sha256="1575c2ab252996ff4c2f0cc5fe697b383e7d21138372d9e544b921bebc3970aa")
	version("0.3.6", sha256="56c69ffcbd7bd266857deb76a85be74cf5f177ee2b60603a27dfb7d210370e38")
	version("0.3.7", sha256="5397b50aa1218450ac111a3c4053cdf761e684232ce70e2f6e8e0173fef3d598")
	version("0.3.8", sha256="678d0837344c3195408f250cc44d3575aaf59444176570f88d75c7eaac282fb2")
	version("0.3.9", sha256="cd862d4ef05acffddb142d676c77bd6fca9d8451b6cdff931946210c1c74d346")
	version("0.4.0", sha256="187156d7ebace5b6d2c51ce9675294dadee9bb3fd7ea2924b09cb10e0006c35c")
	version("0.4.1", sha256="d257246844474dcdc2d5b582e71663a010e8ecd7fcb3d4a8b3390aec33320c81")
	version("0.4.2", sha256="75499158856d5304a04b4144d49efb50b0f02d92ed622ed6e508b8fa146f57f7")
	version("0.4.3", sha256="0d6ecdbf754924c4f65022b453b88470dc95d4ff943d75c39b004cbe8b63d0c7")
	version("0.4.4", sha256="2d1a5ab08e2c200c2a191735316f6d1e74fa3a37da143d75f17a98b6cb55dff5")
	version("0.4.5", sha256="ecd08fae680a479b573587c8d512b3016df80c68810ff3953c77ecae212abbdc")
	version("0.4.6", sha256="9172d4531368498e6b80c6ead5a08a78d5cdb0a159333f0170c6e8e799a7f056")
	version("0.5.0", sha256="0bc4fd3ad1928489f70a81804e965586c86805673a7d951dc3358b7487b4f36e")
	version("0.5.1", sha256="37d17adc9e71386c59b28f4ef5972ef6fe0023714fa1a652b8edc83f7ce0654c")
	version("0.5.2", sha256="1d2bdf373e3e6cfbdc113d4e91547d3add3774d8722c8d4f225fa39586fb8076")
	version("0.5.3", sha256="857af6169d90e4a0a814130b9b107f5d611150ce440107e1c1233521c6fb1e2b")
	version("0.5.4", sha256="03827a9fca8b5c540305c0844a62591cf35a0caec199cb0f2f0a4a0fb15d8f24")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("opencv+python3+imgproc+imgcodecs", type=("build", "run", "link"))
