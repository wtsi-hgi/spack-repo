# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLevenshtein(PythonPackage):
	"""Python extension for computing string edit distances and similarities."""
	
	homepage = "https://github.com/rapidfuzz/Levenshtein"
	pypi = "levenshtein/levenshtein-0.27.3.tar.gz" 

	version("0.12.0", sha256="1407b49f4cc47d2d952e5bc2df562178da2e38d618fa1b3e508bede50ff9dc32", expand=False, url="https://files.pythonhosted.org/packages/bd/94/f40c732bbe3fd01df7c96b165359f73149b1fa0748993f769b5d2a513c8d/levenshtein-0.12.0-cp39-cp39-manylinux1_x86_64.whl")
	version("0.13.0", sha256="2e291ddf36c023c1a457eec7b9df6aa600c17dc0b6abdb9bd27e980f461fc0a5", expand=False, url="https://files.pythonhosted.org/packages/95/75/107bfcbad8a9cde0585598be70936f510a11c2ff95f61778f104430dc380/Levenshtein-0.13.0-cp39-cp39-manylinux1_x86_64.whl")
	version("0.14.0", sha256="f49207d6c1bbd23e5309880d774ecb03ecf93e979e8a0c2be221bf4b5aeace97", expand=False, url="https://files.pythonhosted.org/packages/ef/7e/d43e54024f73597c5eb454f84d50533d8dee4dc8adc3091e321c6d0cedc7/Levenshtein-0.14.0-cp39-cp39-manylinux1_x86_64.whl")
	version("0.15.0", sha256="3ca472c9d2c80f908c03b6761fe6eb5c9acb982f99c68b542672eda48bae6ec4", expand=False, url="https://files.pythonhosted.org/packages/b9/8c/1145d91b1bf87f12d5def966a289b397588503a917b000ff54f362ff9466/Levenshtein-0.15.0-cp39-cp39-manylinux1_x86_64.whl")
	version("0.16.0", sha256="1cfdf50304b3d8454ce0bb662e3c7810997d599fc5f232ed3ad4effd4a3505b5", expand=False, url="https://files.pythonhosted.org/packages/32/98/0eb59535fee1bdf1e6b74f86bbb4e6681fdcfe207a0e2c79c1d5a7608133/Levenshtein-0.16.0-cp35-cp35m-manylinux1_x86_64.whl")
	version("0.17.0", sha256="b520f1f0049c361bbeaace1ae22c022b281c0e6205bac43c1818b65e5a4da924")
	version("0.18.0", sha256="1fa92494f4d7e77cb7f05a1240cf125713372b29d9ee1c223f77f34104278dec")
	version("0.18.1", sha256="c9bda0d6daaec0635f4562eec00e68f3d289557c4259e8c8277b6942108764e8")
	version("0.18.2", sha256="24d13db1c0830fcca8510f324c0f809b6610f827c6ae9fb106d2a8d10320af94")
	version("0.19.0", sha256="9f97bb33936c93e7573dc4982eed9dae6adc6522e47f0c0189b2eb150586388d")
	version("0.19.1", sha256="2f75276bf52b7cb9adbd8ff8c9358423359c4afa08bb7ee9d2cb30e0994d3e79")
	version("0.19.2", sha256="d7b0744907bdd143750a6d484b17494b18a19a97864373dfd6bcb896480555fc")
	version("0.19.3", sha256="b61ef578876e7500e9077b08331a434d06c50d076669e3becba2ce26ebe21a93")
	version("0.20.0", sha256="184e95c4c83e054a0eb4d50f76ec5fc9f2c202b5491e2366b1cb58bd77658e2a")
	version("0.20.1", sha256="75c5f64595955f323de84c5d8cf3a6896b7bd978d53bf48af61bcfefc850161e")
	version("0.20.2", sha256="e1528eb56d74146582aa4180a71c8808f0428fa0e08812c39923cac97faf414a")
	version("0.20.3", sha256="9f7fb9d4e64e9663c2bed51e5c6beca4e88d62d30a5072b2e805ade09adf9acc")
	version("0.20.4", sha256="a5cc10560d71a47bcc4f5f2ffbd3f69ffe9cd293126e1dc81ad7278c393ea388")
	version("0.20.5", sha256="cc5cfce70b40e4ccbcadbeac3fc10c14db18766822c9d671f6d9cbc7c6dd031c")
	version("0.20.6", sha256="4ec8380f15e8e30fa0cd2d982563467e5d14e6f33e762b10fc15fe66c68a3b12")
	version("0.20.7", sha256="b26fb439a7fbb522af63bbd781fbf51ec0c0659134a93f5bc8e9e68641df811e")
	version("0.20.8", sha256="a8cc52849264d3aa6e16c9daca95a02d59e9496c86f18def7131413cfba617cc")
	version("0.20.9", sha256="70a8ad5e28bb76d87da1eb3f31de940836596547d6d01317c2289f5b7cd0b0ea")
	version("0.21.0", sha256="545635d9e857711d049dcdb0b8609fb707b34b032517376c531ca159fcd46265")
	version("0.21.1", sha256="2e4fc4522f9bf73c6ab4cedec834783999b247312ec9e3d1435a5424ad5bc908")
	version("0.22.0", sha256="86d285d770551cb648d4fcfe5243449a479e694e56b65272dc6cbda879012051")
	version("0.23.0", sha256="de7ccc31a471ea5bfafabe804c12a63e18b4511afc1014f23c3cc7be8c70d3bd")
	version("0.24.0", sha256="0cbcf3c9a7c77de3a405bfc857ab94341b4049e8c5c6b917f5ffcd5a92ff169a")
	version("0.25.0", sha256="0bca15031e6b684f82003c9a399172fac6e215410d385f026a07165c69e75fd5")
	version("0.25.1", sha256="2df14471c778c75ffbd59cb64bbecfd4b0ef320ef9f80e4804764be7d5678980")
	version("0.26.0", sha256="960b020d96bbd348400d6ff5c16290adee49f0ae2d42707a550a3b4f7d092abe")
	version("0.26.1", sha256="0d19ba22330d50609b2349021ec3cf7d905c6fe21195a2d0d876a146e7ed2575")
	version("0.27.1", sha256="3e18b73564cfc846eec94dd13fab6cb006b5d2e0cc56bad1fd7d5585881302e3")
	version("0.27.3", sha256="1ac326b2c84215795163d8a5af471188918b8797b4953ec87aaba22c9c1f9fc0")

	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-rapidfuzz", type=("build", "run"))
	depends_on("py-scikit-build-core@0.10: +pyproject", type="build")

	@run_after("install")
	def install_test(self):
		python("-c", "import Levenshtein")
