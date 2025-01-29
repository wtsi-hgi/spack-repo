# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCrossmap(PythonPackage):
    """CrossMap -- Lift over genomics coordinates between assemblies."""

    homepage = "https://crossmap.readthedocs.io/en/latest/"
    pypi = "CrossMap/CrossMap-0.7.3-py3-none-any.whl"

    version(
        "0.2.3",
        sha256="22ff2de68c9e6b9050a8c5d286348adade1bcaf8630520a8ca2cb53e8eefaa9d",
        expand=False,
        url="https://files.pythonhosted.org/packages/16/92/4499587dcf152223e0cf256184587b479ec65c1fb7f6c93c6f8466fba06c/CrossMap-0.2.3-py2-none-any.whl",
    )
    version(
        "0.2.4",
        sha256="cb100523de591e75710c6eb76b6ff8aa654ed03a64dada94d87d748d81df06dc",
        expand=False,
        url="https://files.pythonhosted.org/packages/44/90/5ed109b5a64ddbacf743851197c2d55e4e3a952351ea4aa4672961cfe421/CrossMap-0.2.4-py2-none-any.whl",
    )
    version(
        "0.2.5",
        sha256="9fd86186bab1215f406fafe495312cc9f763c2046f20501b606317885fa9a8c9",
        expand=False,
        url="https://files.pythonhosted.org/packages/95/3b/b2f4376f5491bad7ff02cf511c68433bd592e35b17fa28cb930ac8e52ae7/CrossMap-0.2.5-py2-none-any.whl",
    )
    version(
        "0.2.6",
        sha256="ec6c0f3c5d0fd3e70edef5505dcdd6b836c032693d4c1b16453487bb6a5454c7",
        expand=False,
        url="https://files.pythonhosted.org/packages/1d/9a/54edc16ac5138add7685e4e218bd79f232796a1285504976a3f2558dcb8f/CrossMap-0.2.6-py2-none-any.whl",
    )
    version(
        "0.2.7",
        sha256="8ab44c46b17243eb382d1c1043c452f8e3cbe67c79a0d92e21f005eb6b1955ef",
        expand=False,
        url="https://files.pythonhosted.org/packages/66/16/510c67508f3c61435b7546df9d397b6a6565c46d3e8d95aef0243b2b38f9/CrossMap-0.2.7-py2-none-any.whl",
    )
    version(
        "0.2.8",
        sha256="50f49a6daae54545a9fd30c94ecc451ad929e6795889748f7b0dfca5e8a0108b",
        expand=False,
        url="https://files.pythonhosted.org/packages/e7/cd/a3a5534f3b091cd4b7bd8b970440151098949ad530f6402731e10e657cf0/CrossMap-0.2.8-py2-none-any.whl",
    )
    version(
        "0.2.9",
        sha256="1abe1235736413bf1d21e73e494dc90dab658dbb222cf108f17187f29f7dbc66",
        expand=False,
        url="https://files.pythonhosted.org/packages/40/fc/a1b6b32ae204c221a24da92aab6082423cd0d95f2c06ae5e1c34e63c3cde/CrossMap-0.2.9-py2-none-any.whl",
    )
    version(
        "0.3.0",
        sha256="7e8d440592f9e4e9b119e922df0778cebcdc3f726eb7bfe9b639d35ad2d35ee4",
        expand=False,
        url="https://files.pythonhosted.org/packages/36/24/b8f162d197c51c51f5e89be7f0c8d86fed929602a24a6ea0149145eed258/CrossMap-0.3.0-py2-none-any.whl",
    )
    version(
        "0.3.1",
        sha256="d4fd35614d294453b18067082d67bf952183d4bc8557d7d42a29ff7bca6e06f5",
        expand=False,
        url="https://files.pythonhosted.org/packages/48/7d/b6cd5e5683c70ad81c9a510040e3847539ca5e5634db05bba713c7518aeb/CrossMap-0.3.1-py2-none-any.whl",
    )
    version(
        "0.3.2",
        sha256="3715ba7181a757b3160d95a49c482e25e05ba475d40b9d8c59152c914709ef91",
        expand=False,
        url="https://files.pythonhosted.org/packages/07/77/71291fb20050c23583d30f046abaec88945be55b8dc1b35dea4a08966d74/CrossMap-0.3.2-py3-none-any.whl",
    )
    version(
        "0.3.3",
        sha256="234710bf96482866686cacec46aac1229049ee827050f6991ce13bcbb3ea12da",
        expand=False,
        url="https://files.pythonhosted.org/packages/2f/8f/4beb4d8bb30144ef619cc7c3b7331e2b29e133fde10fb65561b1c2ab95cc/CrossMap-0.3.3-py3-none-any.whl",
    )
    version(
        "0.3.4",
        sha256="dd03075c7da521804690591f5993301a675d35444e4e99cd42bf514e4e4a836c",
        expand=False,
        url="https://files.pythonhosted.org/packages/79/87/cec8b77f3818fb800fb0adf5382a106db39272a3de860e9b9d8fad747219/CrossMap-0.3.4-py3-none-any.whl",
    )
    version(
        "0.3.5",
        sha256="0d035c73f7d38f2e4d368b59eb62faf42e4380f4642f0ae40ec2da2b6bd69975",
        expand=False,
        url="https://files.pythonhosted.org/packages/4e/38/de2e9e4383a4ee8bd0213fd3bbf237eea5418c56eb3de2e94b0b9677bfd6/CrossMap-0.3.5-py3-none-any.whl",
    )
    version(
        "0.3.6",
        sha256="d0113d05191722a64dac399e468e6b3a7a796e967b63b72f300aa0702bac95a2",
        expand=False,
        url="https://files.pythonhosted.org/packages/6b/cd/0daa95bb617597a66b4f351f3932a45d24b598c22c27b39412d78cbd0506/CrossMap-0.3.6-py3-none-any.whl",
    )
    version(
        "0.3.7",
        sha256="8a867f11b2e6011cbc6efe09601dc56995e00d7a3119cda257daaa4fd56ecd3a",
        expand=False,
        url="https://files.pythonhosted.org/packages/8b/23/aa4e5414d43922642b9228700ac9f65ea7658fab15b0bdacdca7214f112d/CrossMap-0.3.7-py3-none-any.whl",
    )
    version(
        "0.3.8",
        sha256="96bee8755f2a876bb0e9fb5a6411190543d598411e8847dd4c1e2999fae26972",
        expand=False,
        url="https://files.pythonhosted.org/packages/50/98/eeeedb87d4d49e2f52019a65b7966e0732d257517dea80cd70a8d1b155bf/CrossMap-0.3.8-py3-none-any.whl",
    )
    version(
        "0.3.9",
        sha256="99b18b1b663f40840536668bc0b962f1d7d3d03c29454f7b6cf7bd86a584ce07",
        expand=False,
        url="https://files.pythonhosted.org/packages/18/a5/d4302837a655ade7c53ee9fd6178a55077e918cc9dd23197ac010cd3e133/CrossMap-0.3.9-py3-none-any.whl",
    )
    version(
        "0.4.0",
        sha256="aac527692ca1997611ff4ee1e2fe1064664c8e34fafce56393737dabfd47a4c5",
        expand=False,
        url="https://files.pythonhosted.org/packages/94/74/5b81aa91ef464cdf9419d1f483aba14d0b31a99efaea72fad4c0fb578202/CrossMap-0.4.0-py3-none-any.whl",
    )
    version(
        "0.4.1",
        sha256="2fbeddaaad951680bae81df6e2e5c33b3cd3a5f4c30c3926d7ef0f12b5d038cf",
        expand=False,
        url="https://files.pythonhosted.org/packages/a1/3f/f95f033cec671f062d0ae6cfe6bd914e2bf9474b2a3cff345f043274d4d8/CrossMap-0.4.1-py3-none-any.whl",
    )
    version(
        "0.4.2",
        sha256="d8607a577dac61e30a44ee42760c5fb8765d3dc9c2529a923e1bc885fe688851",
        expand=False,
        url="https://files.pythonhosted.org/packages/6e/ed/c30a3e3621a59f253e3493bef34d0d272c52a332fc140737d3a032240cb3/CrossMap-0.4.2-py3-none-any.whl",
    )
    version(
        "0.4.3",
        sha256="d0d958d9e2efe9ddf476688f9e33c4b53743a946de130beefee207f306f8003f",
        expand=False,
        url="https://files.pythonhosted.org/packages/0e/0d/0579454dd14d00ee2465bfd9dfeff06860ceddcefbe382c1c84bab8d5b22/CrossMap-0.4.3-py3-none-any.whl",
    )
    version(
        "0.5.0",
        sha256="9c4eb3ffed3d97fa8132bee6b2d767d4936f70cb0a1b7654b2da7ba6b8dfe5a2",
        expand=False,
        url="https://files.pythonhosted.org/packages/2f/d8/6cef0676c1a8fd7d4bb53ba2262158b8002e751499372d348039c82176a2/CrossMap-0.5.0-py3-none-any.whl",
    )
    version(
        "0.5.1",
        sha256="d78939116614121d50d91994ce9dd65b0220f41b804af17c92e05c48f18de27c",
        expand=False,
        url="https://files.pythonhosted.org/packages/f6/b4/517f994e997cec0b99d517ffd6f78e02e4eab5c4a8c1779dced73144b26e/CrossMap-0.5.1-py3-none-any.whl",
    )
    version(
        "0.5.2",
        sha256="c47bb52ff50b5a29484c864ef2040096bd7f39dcaacec0225daec51ca0f11342",
        expand=False,
        url="https://files.pythonhosted.org/packages/16/d5/8d949d09405c85ee7b316625fccd6a99a6dd68f7ab13a490325fc2bad2d8/CrossMap-0.5.2-py3-none-any.whl",
    )
    version(
        "0.5.3",
        sha256="5d0bcef2582a0adabc7981865a9563a54fcd084c74086f4880f705f740200901",
        expand=False,
        url="https://files.pythonhosted.org/packages/a9/a5/1c1a162630f3a8335d6f3bbc02fc1c7a6f48ab7c1344424eb37523a4b4de/CrossMap-0.5.3-py3-none-any.whl",
    )
    version(
        "0.5.4",
        sha256="c17642a8a725cb51e30e73ece8a6b661ba2ecfd8cef6d7940436c8d32bb104e4",
        expand=False,
        url="https://files.pythonhosted.org/packages/cd/de/642fed805b329e1cafaa909f54013b83ac010ef61f2436b29cb3a581be5a/CrossMap-0.5.4-py3-none-any.whl",
    )
    version(
        "0.6.0",
        sha256="b7894df9c862f99a80b57fcbd0649791c240b0b7758d1d347b5f1a561cadbc0a",
        expand=False,
        url="https://files.pythonhosted.org/packages/e9/c9/de0ed294c32112a8f0fb00b206b39136f34c873293c5cab52f207849df29/CrossMap-0.6.0-py3-none-any.whl",
    )
    version(
        "0.6.1",
        sha256="aebd411f469fb9f2a880b8d34fca74cdb3fe7976ba252f5a000ff98a667be0e6",
        expand=False,
        url="https://files.pythonhosted.org/packages/a3/59/837fe9146f288b781c15aa4061f786a81d452a30570d2e3cb5a4809fa3c4/CrossMap-0.6.1-py3-none-any.whl",
    )
    version(
        "0.6.3",
        sha256="2813050a601849f0e635b400269d372f3c39cf4ee02a1237cc211062f920c4f5",
        expand=False,
        url="https://files.pythonhosted.org/packages/9b/1b/7adfcb422950c2da7423f5d33e519e3d8e8b9147bf7d8e68718bc75b2468/CrossMap-0.6.3-py3-none-any.whl",
    )
    version(
        "0.6.4",
        sha256="f1a975f89eaf7445cd0d0252c7b11ea25825f474341c67ca6312752f42e2f3b8",
        expand=False,
        url="https://files.pythonhosted.org/packages/24/b7/95906ab3a4c604e5804cfd2d9c3eb321cd3c3681c05ea73c3d9bcaf1baa1/CrossMap-0.6.4-py3-none-any.whl",
    )
    version(
        "0.6.5",
        sha256="be9f1e16b90c2fc715f804227bf4f30cd784cd13c38a1bce928ce14b6d56df03",
        expand=False,
        url="https://files.pythonhosted.org/packages/d1/34/4897f57863ca2ec4afd2347f3accc8b4fc57145c6d2ed44f0c7231431812/CrossMap-0.6.5-py3-none-any.whl",
    )
    version(
        "0.6.6",
        sha256="e95d677a965e7c73309679e6f2979b39393560821f452f1e75ea7449d720e7cc",
        expand=False,
        url="https://files.pythonhosted.org/packages/15/74/3e436ea58c927eb92d7ebbc607c674759c47e9a60e672cc66dda5d65c932/CrossMap-0.6.6-py3-none-any.whl",
    )
    version(
        "0.7.0",
        sha256="c4e1697370b5f93f3f80b2e201e34b968024a8c4b6f2635ba12ec20d0edb244b",
        expand=False,
        url="https://files.pythonhosted.org/packages/2c/be/af636efe2c84e84ccc1f7edabe15bafba1b352ee3812203c1f8e688003ad/CrossMap-0.7.0-py3-none-any.whl",
    )
    version(
        "0.7.3",
        sha256="9d501015378b6d77a79475343ae2aeb9c3b0430dc2ef5d41f7e774b9de8d5ffe",
        expand=False,
        url="https://files.pythonhosted.org/packages/e7/01/1b79ccbf9b119da5983ae1d5b4012fa1d3ec5180616168d49e732d902a4b/CrossMap-0.7.3-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-bx-python", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-cython@0.17:", type=("build", "run"))


# {'bx-python': ['0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8', '0.2.9', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0', '0.7.3'], 'cython(>=0.17)': ['0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8', '0.2.9', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.3', '0.6.4', '0.6.5', '0.6.6'], 'pysam': ['0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8', '0.2.9', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0', '0.7.3'], 'pyBigWig': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0', '0.7.3']}
