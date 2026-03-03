# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySas7bdat(PythonPackage):
	"""A sas7bdat file reader for Python"""
	
	homepage = "https://bitbucket.org/jaredhobbs/sas7bdat"
	pypi = "sas7bdat/sas7bdat-2.2.3.tar.gz" 

	version("0.1.0", sha256="fdf2556fa78ddaffb2195ee86c088dfdfd8f4d97c0a3fc96242b60dd9b9971be")
	version("0.1.1", sha256="76b952df197d3f20ecd433c6c84dd0849cc48204309ee8f2bc596017a03af926")
	version("0.1.2", sha256="dfebbe8317663d004076f156a155114fed4d399420ff4443ac5d82ceb2c49ad9")
	version("0.2.0", sha256="121c6f8c72c0221aa1310c0d827a3d74d3b9130e6351201283da3f810efaf002")
	version("0.2.1", sha256="fee7bb690d094c292f5963701b9fbc1fd742689183c4ab9e09c7b9a39f0b2a0e")
	version("0.2.2", sha256="b55ae23db56e2c9a1c8657b03e0c3dbddfdb77f740ed036334b98b45df9f1510")
	version("0.2.3", sha256="844ecca90c1d95f2c66641094fa85122d46c0b2c01a2f413ef083ba88d630252")
	version("0.2.4", sha256="d54feb5b3aba5c958a7c9d9548c30875e3829710f70450a0662ab2fc80e7dbc0")
	version("0.2.5", sha256="f634c1a1433bbc3829fda4f734bda6b0a292645935a6462a9b9e7f60b7ab9820")
	version("1.0.0", sha256="0b3e585d809ed4995c21cdb6bd70546869221384665811af2d68f360bc1719ea")
	version("1.0.1", sha256="52a5601b27074a74a3e983813f28823ceb605e6594b9730d4d5103d86ae6a0da")
	version("1.0.2", sha256="1a1f660044d67a9d9bd76668dfebadfe7dd6c9a555268001f1768fdf57e98abe")
	version("1.0.3", sha256="8c7917121f9d76a5684123d03d47d6ca8353eb3988b5e384f2641081e870b155")
	version("1.0.4", sha256="13016dcdbb68e7976f5a79538b2844aa01e08953088f47dde7870c0362d1071e")
	version("1.0.5", sha256="bdb23a92faba21f6ec183cffc81fcb6e9eb0a7d03294b930fa05952e805450eb")
	version("2.0.0", sha256="3709bbe3b156ab2b9f466aba78d4b23a953214869b64669a3c7531b968f30609")
	version("2.0.1", sha256="c4315e9fbb333ddcdb0c83acd408f5c5a56c6402e8fe67ee37c0b63a8204ed1b")
	version("2.0.2", sha256="d11a68d4d5b242d5acc51ff1bbd51b5c00141e972df4fa2fff7c9f459df0e62a")
	version("2.0.3", sha256="f620282f954d1179520b95fc1f984e6cb9dff5a7fd327ada462ccbcc12d8ae74")
	version("2.0.4", sha256="15810552c2157c36e78ce67ac9d6060eaed58084a2b4b089c15286fcc1ad4394")
	version("2.0.5", sha256="5c1dc804a7b6faf17b64efcd724d3cca1878e43b76566c93f48a9aafc7e2aa92")
	version("2.0.6", sha256="dc6212162d18bb414aa781bfd0ad21b908b274728ee07998eb36fd9938ee1a96")
	version("2.0.7", sha256="f1f0a95183c5a8cf8e4d378b1ed5778853a08e9f5eab42381a410368801a94c2")
	version("2.1.1", sha256="2cf6ecd40bdde1e4e9cc71813489b523b0d2e27a2c282396120a58314b4e3fae")
	version("2.1.2", sha256="6f11f8a812f860d27efa418a9b981d2f825466b973f750a15cc3ada57c0c46c6")
	version("2.2.0", sha256="f927bed44abf5d2930ab0ed7b43f0b4af53151cb820ee39f1e58219e9ebadec1")
	version("2.2.1", sha256="9bca352b07a61686eb2b4d636560b5a7ffc1e2004d5e7275968b2fc277615679")
	version("2.2.2", sha256="fea44a95e0db614088493de28b94afe8471b9e1fd4d6d5cabc56c83664793855")
	version("2.2.3", sha256="484c609d962442203c15bc719a638de992a23cd13bc1971a5af6dfb0daf9f797")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-six", type=("build", "run"))
