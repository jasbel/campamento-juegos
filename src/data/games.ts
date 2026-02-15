import gamesData from './games.json';

export interface Game {
  id: string;
  title: string;
  description: string;
  materials: string[];
  type: string;
  category: string;
  tiktokUrl?: string;
  image?: string;
}

export const categories = gamesData.categories;
export const games: Game[] = gamesData.games;

export const getCategoryById = (id: string) => {
  return categories.find(cat => cat.id === id);
};

export const getGamesByCategory = (categoryId: string) => {
  return games.filter(game => game.category === categoryId);
};
