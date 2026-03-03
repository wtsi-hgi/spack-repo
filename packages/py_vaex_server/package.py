# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVaexServer(PythonPackage):
	"""Webserver and client for vaex for a remote dataset"""
	
	homepage = "https://www.github.com/maartenbreddels/vaex"
	pypi = "vaex-server/vaex_server-0.9.0-py3-none-any.whl" 

	version("0.1.1", sha256="34b222ff775262eeeb4b02575d3b12b8e508dd31fef28e5781019798f8e90e44")
	version("0.1.2", sha256="f7d861017f5429d8a2ef621fc895c68471a2ec4ef237304c8b9c3ac6ff547aae")
	version("0.2.0", sha256="a07c8fce55daa8f795f3c59fd05cff2eb22359460ced95738422d52aa28383db")
	version("0.2.1", sha256="658bf3eb3cc859f693e5ef8c5efe806f8db3d3bc3676bfd8389cb0f50822e005")
	version("0.3.0", sha256="8174fd14132c37f113fd9096f468d74b04355e91e9adc3cbec5f8749b1f7a7f2", expand=False, url="https://files.pythonhosted.org/packages/df/8f/4c1a4601c5643188d1ef6e569a9fc29536229286008b8a943a152fe81cea/vaex_server-0.3.0-py3-none-any.whl")
	version("0.3.0a1", sha256="983dadd9b64d5644ae190d3774c595740ef50e0eec5b24c389d2eb41f97b8007", expand=False, url="https://files.pythonhosted.org/packages/dd/8b/9550c2012a03a2958ae51a863487a4e790d8c141833049cd1824026c8fb7/vaex_server-0.3.0a1-py3-none-any.whl")
	version("0.3.0a2", sha256="34980cea09d76725d4f2b00682bd90e302c405cb20a852fa0717ce0ce53318b3", expand=False, url="https://files.pythonhosted.org/packages/0f/86/c3d8dfe84e961d8ad53775e2ecf77f539e83871c7dd61ec61c96e2b8234f/vaex_server-0.3.0a2-py3-none-any.whl")
	version("0.3.1", sha256="5b7d5a54f2aa3c91baddcdbbb3cd28d745de72984d11dc2dbc8a31b029a971f5", expand=False, url="https://files.pythonhosted.org/packages/f2/40/576ac1e9a64240970e7e20b98788f292f043c3cff2ff118c7a3a557dc548/vaex_server-0.3.1-py3-none-any.whl")
	version("0.4.0", sha256="a64a35030ed3a365a2f7714237a37f49354e4fd792f17078f0a478ba3db68d93", expand=False, url="https://files.pythonhosted.org/packages/a2/41/29861d3dce92a1ae3232ae110b50e7a1b68af761fa149dc68371d135e6c5/vaex_server-0.4.0-py3-none-any.whl")
	version("0.4.0.dev1", sha256="6e4e0a9e652d386227ba2b08746939a6ba0c83ccc6bcc6c0b47102f824d2a8e9", expand=False, url="https://files.pythonhosted.org/packages/8e/ae/12c67c7612f2432e981ee77bce458f43972d6a6a0b3b77a028d6d7620ace/vaex_server-0.4.0.dev1-py3-none-any.whl")
	version("0.4.0a1", sha256="baf6ca928a321e3d2936cfa06c46c9c9aee82a5cb0f59b2b1d0062cdbff66f85", expand=False, url="https://files.pythonhosted.org/packages/dd/25/fa3368de1e96ff6330d2fcc9625409fe020402abd9517665cc5f2d481eae/vaex_server-0.4.0a1-py3-none-any.whl")
	version("0.4.0a2", sha256="d941ee63fddcf4614b5fb7a472a24875d8b8690b62cb1d8eb8101c4e1878e532", expand=False, url="https://files.pythonhosted.org/packages/62/11/9bf67c018d8fcc413531a89ebde7a200da7d2e3f981f6ea1ec5e8db21f7c/vaex_server-0.4.0a2-py3-none-any.whl")
	version("0.4.0a3", sha256="a34602e3df68b88a8699f53c6c06a7c33bca69b4402dc28ca1e1a2d2a4ffc3af", expand=False, url="https://files.pythonhosted.org/packages/97/eb/fa0254869fe98ae7b39dc21e79adb3850a8e372ee8ad582849e904abeeeb/vaex_server-0.4.0a3-py3-none-any.whl")
	version("0.4.1", sha256="7f875fcd9bbc3689ae0eeaabd2e83703bcec0c65eb37c6dcd9bf0cf4b96f9b55", expand=False, url="https://files.pythonhosted.org/packages/23/9c/d8ec1a7b323df46cb7e88e80996c67a23e4ec168fbb0affadc82900a726a/vaex_server-0.4.1-py3-none-any.whl")
	version("0.5.0", sha256="e359444d2847e0bf0041ba219c71330e7c18295927ae7f084db563151d3e5783", expand=False, url="https://files.pythonhosted.org/packages/59/45/dc843b0d0b8f7faac6d52a55e673220fba6780c93302b24a20490ef1af6b/vaex_server-0.5.0-py3-none-any.whl")
	version("0.6.0", sha256="ed26cab52e690c04768945e14b0b5f44b9f6d63819d5cc401d2426b9d281e499", expand=False, url="https://files.pythonhosted.org/packages/fb/45/84689ca928deb98843c5ee0e34cd583546df5a412e8536bfc681933f8335/vaex_server-0.6.0-py3-none-any.whl")
	version("0.6.1", sha256="a97e6edf2a013fb5a93ba03a84dacba8af644d9ff3d3aab81d0a23d078a47fd3", expand=False, url="https://files.pythonhosted.org/packages/ba/a9/631e7184f5c0690aa18fb06d878fe21347224e8f70f4587366b4b63f2954/vaex_server-0.6.1-py3-none-any.whl")
	version("0.7.0", sha256="72604e4c8776b7853a462751853628db727c874f760ab8214c3be9f59473c1cb", expand=False, url="https://files.pythonhosted.org/packages/0b/5c/e7d8065e4c10a4d8cce1292c539bf763d186fae1303908a6b0809891b7f3/vaex_server-0.7.0-py3-none-any.whl")
	version("0.8.0", sha256="43aabf2158b523fc07102f9df2e63de9985e58451fc601056acf8b54b9eed8fa", expand=False, url="https://files.pythonhosted.org/packages/0c/12/eb80417b0a36f433801ca4e759160501c3cb73249e373bcd233bdb2cf4fe/vaex_server-0.8.0-py3-none-any.whl")
	version("0.8.1", sha256="7c3a3bb954880389452d5ad0038813b3608d2cb182e055ef9cd39d9a8de32b19", expand=False, url="https://files.pythonhosted.org/packages/13/67/0c28303618a0581eaf78ffa333c7088bac11e87a38cbf222970325fb1bdd/vaex_server-0.8.1-py3-none-any.whl")
	version("0.9.0", sha256="11e46056817fc30aaa4a033c24b28066e51707bfa23fe8eca8fe61aca58b83d6", expand=False, url="https://files.pythonhosted.org/packages/20/4e/46587dc09f475527003263ed6b466e2f74ffbc9af9aa50ea0a6dea51d8be/vaex_server-0.9.0-py3-none-any.whl")

	depends_on("py-uvicorn", type=("build", "run"))
	depends_on("py-fastapi", type=("build", "run"))
	depends_on("py-cachetools", type=("build", "run"))
	depends_on("py-tornado", type=("build", "run"))
	depends_on("py-vaex-core", type=("build", "run"))
