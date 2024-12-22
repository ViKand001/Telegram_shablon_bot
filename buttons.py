from utils import get_translation

def get_admin_buttons(language):
    """
    Admin paneli uchun tugmalar.
    """
    return [
        [get_translation("manage_users", language), get_translation("send_advertisement", language)],
        [get_translation("manage_channels", language), get_translation("show_statistics", language)],
        [get_translation("exit", language)]
    ]
