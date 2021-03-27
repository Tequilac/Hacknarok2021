# General settings
from dataclasses import dataclass

import pygame
import os
from dotenv import load_dotenv
from pathlib import Path

pygame.font.init()

# General
WINDOWS_SIZE = 1000, 1000

# Menu
MENU_FONT_SIZE = 50
MENU_FONT = pygame.font.SysFont("calibri", MENU_FONT_SIZE)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


# Paths
@dataclass
class Paths:
    APP_ROOT = Path(os.environ.get('APP_ROOT'))
    RESOURCES = APP_ROOT / 'resources'
