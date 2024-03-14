# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPandasSchema(PythonPackage):
	"""A validation library for Pandas data frames using user-friendly schemas"""
	
	homepage = "https://github.com/TMiguelT/PandasSchema"
	pypi = "pandas-schema/pandas_schema-0.3.6-py3-none-any.whl" 

	version("0.1.0", sha256="90fd5214e03b0dfa88becfb7de5dd7b0a278658418484ff1a63cfd546ba10797", expand=False, url="https://files.pythonhosted.org/packages/85/d6/2917c4f7a4a45b8a2893a321610d7926696f58ec2a2e84e2e30310c2a206/pandas_schema-0.1.0-py3-none-any.whl")
	version("0.2.0", sha256="4ebaf02e583e4764c040feda52dccc8cf4ef3b0301bebdbefeffe8d84443c22a", expand=False, url="https://files.pythonhosted.org/packages/de/f6/0c6098bd13c6daed642d2b05983d400904fb8b0a3494ee5ba694d75277b1/pandas_schema-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="0b6d2953f744bcc6871cb35c0ef9d6de509a04b4289ac6140a9ec68d4f65470e", expand=False, url="https://files.pythonhosted.org/packages/f5/60/f00e957d92b231d049159008cafc9257a6e696a9ddab3cb6d571b24f2e62/pandas_schema-0.2.1-py3-none-any.whl")
	version("0.3.0", sha256="da82fdfa54ff128d055e89c18b3bfbcb9524772f68488b4b3e7ce8a4320c87ea", expand=False, url="https://files.pythonhosted.org/packages/91/88/729f6c138e1b083db1a14fe31a57c0fe70f1ff805cb28359fb6179e99bf5/pandas_schema-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="61d2d19350989f56d19d3b4c65049dc40035b9c792812c7de0b01894b8def157", expand=False, url="https://files.pythonhosted.org/packages/f2/8c/5aef19521e6a1d2006721497acbb100ef93d13602cc93da3ccc56a4a6e18/pandas_schema-0.3.1-py3-none-any.whl")
	version("0.3.2", sha256="d1e5ac4b3794e5d7b5cbadd91c1a61453459356c1c4915804f17f781e2a99b45", expand=False, url="https://files.pythonhosted.org/packages/45/ac/c41262d809a9935668503108ed9d09283759ec3942c01bad9d103cba7643/pandas_schema-0.3.2-py3-none-any.whl")
	version("0.3.3", sha256="74f499b428c25322b6198c269fe42c6a74d0ba9f7d0aee0713445240ba745a2d", expand=False, url="https://files.pythonhosted.org/packages/3e/f8/090e00bbf4de86d2c608f21235d96b0e867c26a6134fe679c4e1dd8d73a1/pandas_schema-0.3.3-py3-none-any.whl")
	version("0.3.4", sha256="33043e8bc102b28cde641a7c73466f725e19d73f198c514a1bbfc6cd9c85d204", expand=False, url="https://files.pythonhosted.org/packages/59/19/33bb47cc354a540980a6f3ec5a15d69cca5fbb240eecced4524c4e934e0c/pandas_schema-0.3.4-py3-none-any.whl")
	version("0.3.5", sha256="2018a5843f9a8facfcf9332d557eb29dcb5f0758b8ba124d137d021a6e633f74", expand=False, url="https://files.pythonhosted.org/packages/9c/03/6d87ce8719dc57e44688096c05fb0efa61a08c6838816c9d991b1ece5b24/pandas_schema-0.3.5-py3-none-any.whl")
	version("0.3.6", sha256="7497621cdf8c191fca1ef6ded9caa6f2153b220f120a2686d921f80c8031994d", expand=False, url="https://files.pythonhosted.org/packages/a5/89/c2e12a52a7baa51fff89055b6c949bd7796ee4ba8432ec1af3c08e25d061/pandas_schema-0.3.6-py3-none-any.whl")

	depends_on("py-packaging", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))

# {'numpy': ['0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6'], 'pandas': ['0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.3.3'], 'pandas(>=0.19)': ['0.3.4', '0.3.5', '0.3.6'], 'packaging': ['0.3.6']}