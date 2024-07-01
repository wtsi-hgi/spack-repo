# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGrpcGoogleIamV1(PythonPackage):
	"""IAM API client library"""
	
	homepage = "https://github.com/googleapis/python-grpc-google-iam-v1"
	pypi = "grpc-google-iam-v1/grpc-google-iam-v1-0.9.0.tar.gz" 

	version("0.10.0", sha256="eeb093be602d9c9df0727fffb60f7569f64752cc2a7cae1e85b8903ada67d3ed")
	version("0.10.1", sha256="9888220c055dc4bfe4d2894f823c17f6194a431444637fede85e9f0058a3d39b")
	version("0.11.1", sha256="27887bad756a50dd333d96028b77bfe9f3ad97a653cca8b0dbcdfa0d7569ca6b")
	version("0.11.3", sha256="e368045d7549254d7b7ed6db8c4cbc932d33624b632501980390f8c567071999")
	version("0.11.4", sha256="5009e831dcec22f3ff00e89405249d6a838d1449a46ac8224907aa5b0e0b1aec")
	version("0.12.0", sha256="0a272e305284bdc23a0129210d8ec4aff7c2d1ac0b16fb37e01ac240b6310fdc")
	version("0.12.1", sha256="ac1ac6d9e5029f7cb17374c9d64a9207ed79de19fca42886f6dc3e8f18c2ccb3")
	version("0.12.2", sha256="bf99f77f7011e6bd877f931aa7fa30735030f8b4ebfa44482b5ebe016cf4c16d")
	version("0.12.3", sha256="0bfb5b56f648f457021a91c0df0db4934b6e0c300bd0f2de2333383fe958aa72")
	version("0.12.4", sha256="312801ae848aeb8408c099ea372b96d253077e7851aae1a9e745df984f81f20c", expand=False, url="https://files.pythonhosted.org/packages/49/cb/5c7a8cf8211475908b9d101d160f02b9fb3f3062302625227e8724db36b3/grpc_google_iam_v1-0.12.4-py2.py3-none-any.whl")
	version("0.12.4b1", sha256="9752dcb0394f8fe909f05dd37f1bb04afa11676315a2a20ea11059c466ade571", expand=False, url="https://files.pythonhosted.org/packages/7b/b6/a832b74c6c1290ad34dde332d7c473511a5a21250cb4e6a0c1b81764bfd9/grpc_google_iam_v1-0.12.4b1-py2.py3-none-any.whl")
	version("0.12.6", sha256="5c10f3d8dc2d88678ab1a9b0cb5482735c5efee71e6c0cd59f872eef22913f5c", expand=False, url="https://files.pythonhosted.org/packages/34/72/c84e54991d452942c5a85474693c8433169104a596e9dd23b05c5f091894/grpc_google_iam_v1-0.12.6-py2.py3-none-any.whl")
	version("0.12.7", sha256="834da89f4c4a2abbe842a793ed20fc6d9a77011ef2626755b1b89116fb9596d7", expand=False, url="https://files.pythonhosted.org/packages/5f/4b/404f59d065a410e835576433bc296599ae093460c7724fa5d5ca2354a885/grpc_google_iam_v1-0.12.7-py2.py3-none-any.whl")
	version("0.13.0", sha256="53902e2af7de8df8c1bd91373d9be55b0743ec267a7428ea638db3775becae89", expand=False, url="https://files.pythonhosted.org/packages/66/a0/d27ec874fb0a86b3609b73161a15cf633924888afa05c1673b3ab5a6c3f4/grpc_google_iam_v1-0.13.0-py2.py3-none-any.whl")
	version("0.13.0rc1", sha256="1a8e37e9661e792f9d2968ba70b04d3ee364fda6f002f76d04788f76c7cb4d1e", expand=False, url="https://files.pythonhosted.org/packages/ec/74/6474d80e78bb4ba9efd084b09cad64592eb40277aaf2a98910b8c0fba824/grpc_google_iam_v1-0.13.0rc1-py2.py3-none-any.whl")
	version("0.13.1", sha256="c3e86151a981811f30d5e7330f271cee53e73bb87755e88cc3b6f0c7b5fe374e", expand=False, url="https://files.pythonhosted.org/packages/a8/7d/da3875b7728bc700eeb28b513754ce237c04ac7cbf8559d76b0464ee01cb/grpc_google_iam_v1-0.13.1-py2.py3-none-any.whl")
	version("0.13.1rc0", sha256="cc9faeb11e4c072e03b615957b64a05bb5304db0aa137af8dc2e6cff14787d8b", expand=False, url="https://files.pythonhosted.org/packages/91/c4/d519c975af9f096d3c9cdebd4f5bb1f1aab9749e3b356eb16240a5439a01/grpc_google_iam_v1-0.13.1rc0-py2.py3-none-any.whl")
	version("0.9.0", sha256="bac9eb1bb88e8cde0e7dcc14cdc4c20002f68a7d88c5996ac4cf50acbe437187")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-protobuf", type=("build", "run"))
	depends_on("py-googleapis-common-protos", type=("build", "run"))
	depends_on("py-grpcio", type=("build", "run"))

# {'googleapis-common-protos[grpc](<2.0.0dev,>=1.56.0)': ['0.12.4', '0.12.4b1', '0.12.6'], 'grpcio(<2.0.0dev,>=1.0.0)': ['0.12.4', '0.12.4b1'], 'grpcio(<2.0.0dev,>=1.44.0)': ['0.12.6'], 'protobuf(!=3.20.0,!=3.20.1,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5)': ['0.12.6'], 'grpcio<2.0.0dev,>=1.44.0': ['0.12.7', '0.13.0', '0.13.0rc1', '0.13.1', '0.13.1rc0'], 'googleapis-common-protos[grpc]<2.0.0dev,>=1.56.0': ['0.12.7', '0.13.0', '0.13.0rc1', '0.13.1', '0.13.1rc0'], 'protobuf!=3.20.0,!=3.20.1,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5': ['0.12.7', '0.13.0', '0.13.0rc1'], 'protobuf!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0dev,>=3.20.2': ['0.13.1', '0.13.1rc0']}